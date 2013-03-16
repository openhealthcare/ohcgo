void function initOHC(context, undefined){
	void function initDynamicTextarea(){
		$(document).on('change cut drop keydown paste', 'textarea', function waitForInputResolution(event){
			var textarea = event.target;

			setTimeout(function testHeight(){
				while(textarea.scrollHeight > textarea.clientHeight){
					textarea.rows += 1;
				}
			}, 0);
		})
	}();
}(this);
