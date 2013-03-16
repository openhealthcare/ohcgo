void function initOHC(context, undefined){
	// Expand textareas to contain user input
	void function initDynamicTextarea(){
		// A list of events that can potentially resolve in changed content
		$(document).on('change cut drop keydown paste', 'textarea', function waitForInputResolution(event){
			var textarea = event.target;

			// Execution in 0 ms allows the stack to clear and the native event to resolve, so the test can react to user input
			setTimeout(function testHeight(){
				while(textarea.scrollHeight > textarea.clientHeight){
					textarea.rows += 1;
				}
			}, 0);
		})
	}();
}(this);
