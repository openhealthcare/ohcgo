void function initOHC($){
	// Expand textareas to contain user input
	$(function initDynamicTextareas(){
		$ghost = $('<ghost/>').appendTo('body');

		$('textarea').each(function(){
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
}(jQuery);
