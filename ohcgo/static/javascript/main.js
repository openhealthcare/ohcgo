void function initOHC($){
	// Render script-only markup islands.
	// Like form feedback messages.
	$(function renderIslands(){
		$('[type=markup]').each(function renderIsland(){
			$(this).replaceWith($(this).html());
		});
	});

	// Expand textareas to contain user input
	$(function dynamizeTextareas(){
		// For our hidden DOM needs
		var $ghost = $('<ghost/>').appendTo('body');

		$('textarea').each(function dynamizeTextarea(){
			var $textarea = $(this);
			// Reference to determine content-based height
			var $clone    = $textarea.clone();

			if($.fn.copyCSS){
				$clone.copyCSS($textarea);
			}

			$clone.css({
				height     : 'auto',
				left       : '-100%',
				overflow   : 'hidden',
				position   : 'absolute',
				top        : '-100%',
				visibility : 'hidden'
			});

			// Bind events that can potentially resolve in changed content
			$textarea.on('change cut drop keydown paste', $.throttle(100, function waitForInputResolution(event){
				// Execute in 0 ms allows the stack to clear and the native event to resolve, so the test can react to user input
				setTimeout(function regulateHeight(){
					if($clone.val() === $textarea.val()){
						return;
					}

					$clone.val($textarea.val()).appendTo($ghost);

					if($clone[0].scrollHeight !== $textarea[0].clientHeight){
						$textarea.css('height', $clone[0].scrollHeight);
					}

					$clone.remove();
				}, 0);
			}));
		});
	});

	// The server side handler doesn't like XHR, apparently.
	// As a result we have to do some clever stuff with iframes.
	$(function formSubmission(){
		var $form        = $('form');
		var $ghost       = $('<ghost/>');
		var $listener    = $('<iframe/>');
		var $acknowledge = $('[data-conditional] a');

		// Give an indicator of state in markup.
		// CSS governs appearance, HTML content.
		function Feedback(success){
			return function feedback(e){
				$form.attr('data-condition', success ? 'success' : 'failure');
			};
		}

		function resolve(e){
			$form.attr('data-condition', false);

			// Prevent all propagation
			return false;
		}

		// Bind attributes & events, attach to DOM
		$form.attr({
			target     : 'listener'
		});

		$ghost.appendTo('body');

		$listener
			.attr({
				name     : 'listener',
				src      : 'about:blank',
				tabindex : -1,
				hidden   : true
			})
			// iframes always load once, even if it's nothing:
			// Nerf the inevitable first false positive
			.one({
				load     : function(e){
					e.stopImmediatePropagation();
				}
			})
			.on({
				load     : new Feedback(true),
				error    : new Feedback(false)
			})
			.appendTo(
				$ghost
			);

		$acknowledge.on('click', resolve);
	});

	// AJAX internal pages in
	$(function AJAX(){
		if(!(history.pushState && history.replaceState && window.onpopstate !== void 0)){
			return;
		}

		function injectPage(event){
			event        = event.state ? event : event.originalEvent;

			if(!event || !event.state){
				return;
			}

			var section  = event.state.section;
			var $payload = $(event.state.content);
			var title    = $payload.filter('title').text();
			var $markup  = $payload.filter('.content').html();

			function reveal(){
				$('.content').html($markup);
				$('body').attr('class', section);
				$('html').removeClass('reloading');
			}

			$('html').addClass('reloading');

			setTimeout(reveal, 300);
		}

		function requestPage(link){
			if(link.href === location.href){
				return;
			}

			$.ajax({
				url     : link.href,
				success : function(response){
					var section = link.pathname && link.pathname.match(/^\//) && link.pathname.split('/')[1] || 'home';

					var state = {
						content : response,
						section : section
					};

					history.pushState(state, null, link.href);

					injectPage({state:state});
				},
			        error : function(response){
                                    window.location.href = link.href
                                }
			});
		}

		history.replaceState({content:document.lastChild.outerHTML, section:'home'}, null, location.href);

		$(window).on('popstate', injectPage);

		$(document).on('click', 'a', function filterAjaxLink(event){
			var link         = this;
			var linkLocation = locateURI(link.href);

			// Only for non-identical internal links
			if(linkLocation.origin !== location.origin || linkLocation === location){
				return;
			}

			event.preventDefault();

			requestPage(link);
		});
	});
}(jQuery);
