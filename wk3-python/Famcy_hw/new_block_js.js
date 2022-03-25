function getCursorPosition(canvas, event) {
    const rect = canvas.getBoundingClientRect()
    const x = event.clientX - rect.left
    const y = event.clientY - rect.top
    return [x, y]
}

function connect_mousedown_action(_id, _name, btn_obj_key) {
	const parent = document.getElementById(_id)
	const canvas = parent.getElementsByTagName("canvas")[0]

	canvas.addEventListener('mousedown', function(e) {
		console.log('mousedown', _name)
	    var pos = getCursorPosition(canvas, e)

	    var token = document.head.querySelector("[name~=csrf-token][content]").content
	    var res_dict = {}
	    res_dict[_name] = pos
		Sijax.request('famcy_submission_handler', [btn_obj_key, res_dict], { data: { csrf_token: token } });
	})
}

// function title_click(e, _name, obj_key) {
// 	var res_dict = {}
// 	res_dict[_name] = e.innerHTML

// 	var token = document.head.querySelector("[name~=csrf-token][content]").content
// 	Sijax.request('famcy_submission_handler', [obj_key, res_dict], { data: { csrf_token: token } });
	
// }
