
function resizeme(Obj,ObjWidth,ObjHeight,intSize){
    intYSize=(intSize/ObjWidth) * ObjHeight
    Obj.width = intSize
    Obj.height = intYSize
}

function mOver(obj) {
  obj.style.color="#000"
}

function mOut(obj) {
  obj.style.color="#fff"
}

    $('#o_uploadBtn').click(function() {
    $('#o_uploadFile').click()
    $('#o_uploadFile').change(function() {
        var formData = new FormData()
        formData.append('image', this.files[0])
        formData.append('image_type', "original_image")
        if(formData) {
            $.ajax({
                url: '/catalog/upload_image/',
                type: 'POST',
                data: formData,
                async: true,
                cache: false,
                contentType: false,
                processData: false,
                success: function(res) {
                    if(res.status == 0) {
                        alert(res.msg)
                        return false
                    }
                    $('input[name="o_img_name"]').val(res.image_name)
                    $('#o_image').attr('src', res.src)
                }
            })
        }
    })
})

    $('#wm_uploadBtn').click(function() {
    $('#wm_uploadFile').click()
    $('#wm_uploadFile').change(function() {
        var formData = new FormData()
        formData.append('image', this.files[0])
        formData.append('image_type', "wm_image")
        if(formData) {
            $.ajax({
                url: '/catalog/upload_image/',
                type: 'POST',
                data: formData,
                async: true,
                cache: false,
                contentType: false,
                processData: false,
                success: function(res) {
                    if(res.status == 0) {
                        alert(res.msg)
                        return false
                    }
                    $('input[name="wm_img_name"]').val(res.image_name)
                    $('#wm_image').attr('src', res.src)
                }
            })
        }
    })
})

    $('#bwm_getBtn').click(function() {
        let formData = new FormData();
        const o_image_name = $('input[name="o_img_name"]').val();
        const wm_image_name = $('input[name="wm_img_name"]').val();
        const seed = $('#encode_seed').val();
        console.log(seed)
        formData.append('o_image_name', o_image_name)
        formData.append('wm_image_name', wm_image_name)
        if(seed !== null && seed !== undefined && seed !== ''){
            formData.append('seed', seed)
        }
        if(formData) {
            $.ajax({
                url: '/catalog/encode_image/',
                type: 'POST',
                data: formData,
                async: true,
                cache: false,
                contentType: false,
                processData: false,
                success: function(res) {
                    if(res.status == 0) {
                        alert(res.msg)
                        return false
                    }
                    $('input[name="bwm_img_name"]').val(res.image_name)
                    $('#bwm_image').attr('src', res.src)
                }
            })
        }
})


    $('#bwm_uploadBtn').click(function() {
    $('#bwm_uploadFile').click()
    $('#bwm_uploadFile').change(function() {
        var formData = new FormData()
        formData.append('image', this.files[0])
        formData.append('image_type', "bwm_image")
        if(formData) {
            $.ajax({
                url: '/catalog/upload_image/',
                type: 'POST',
                data: formData,
                async: true,
                cache: false,
                contentType: false,
                processData: false,
                success: function(res) {
                    if(res.status == 0) {
                        alert(res.msg)
                        return false
                    }
                    $('input[name="bwm_up_img_name"]').val(res.image_name)
                    $('#bwm_up_image').attr('src', res.src)
                }
            })
        }
    })
})

     $('#bwm_extractBtn').click(function() {
         console.log('tell me what wrong?')
        let formData = new FormData();
        const o_image_name = $('input[name="o_img_name"]').val();
        const bwm_image_name = $('input[name="bwm_up_img_name"]').val();
        const is_align = $('input[name="is_align"]').prop('checked');
        const seed = $('#decode_seed').val();
        formData.append('o_image_name', o_image_name)
        formData.append('bwm_image_name', bwm_image_name)
        formData.append('is_align', is_align)
        if(seed !== null && seed !== undefined && seed !== ''){
            formData.append('seed', seed)
        }
        if(formData) {
            $.ajax({
                url: '/catalog/decode_image/',
                type: 'POST',
                data: formData,
                async: true,
                cache: false,
                contentType: false,
                processData: false,
                success: function(res) {
                    if(res.status == 0) {
                        alert(res.msg)
                        return false
                    }
                    $('input[name="bwm_ex_img_name"]').val(res.image_name)
                    $('#bwm_ex_image').attr('src', res.src)
                }
            })
        }
})

$('#bwm_extractBtn2').click(function () {
    console.log('enter into function')
    // $('#bwm_extractBtn').click()
        let formData = new FormData();
        const o_image_name = $('input[name="o_img_name"]').val();
        const bwm_image_name = $('input[name="bwm_up_img_name"]').val();
        const is_align = $('input[name="is_align"]').prop('checked');
        formData.append('o_image_name', o_image_name)
        formData.append('bwm_image_name', bwm_image_name)
        formData.append('is_align', is_align)
        if(formData) {
            $.ajax({
                url: '/catalog/decode_image/',
                type: 'POST',
                data: formData,
                async: true,
                cache: false,
                contentType: false,
                processData: false,
                success: function(res) {
                    if(res.status == 0) {
                        alert(res.msg)
                        return false
                    }
                    console.log(res.image_name+'\n'+res.src)
                    $('input[name="bwm_ex_img_name"]').val(res.image_name)
                    $('#bwm_ex_image').attr('src', res.src)
                }
            })
        }
})
