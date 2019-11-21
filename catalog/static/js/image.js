
function resizeme(Obj,ObjWidth,ObjHeight,intSize){
    intYSize=(intSize/ObjWidth) * ObjHeight
    Obj.width = intSize
    Obj.height = intYSize
}

function mOver(obj) {
  obj.style.color="#ff0000"
  obj.style.fontWeight="bold"
  obj.style.cursor="pointer"
}

function mOut(obj) {
  obj.style.color="#fff"
  obj.style.fontWeight=""
}


  $(".dragFile").on("dragenter", function(e){
         e.preventDefault();
     });
  $('.dragFile').on('dragover', (e) => {
    e.preventDefault();
  })
  $('.dragFile').on('drop', (e) => {
    e.stopPropagation();
    e.preventDefault();
    e.dataTransfer = e.originalEvent.dataTransfer;
    var files = e.dataTransfer.files; //获取文件
    appendFile(files, '.list-drag')
  })

   function appendFile (files, listName) {
     for( file of files ) {
       let url = window.URL.createObjectURL(file);
       let liStr = `
         <li class="list-group-item">
           <div>
             <img src="${url}" alt="文件" />
           </div>
         </li>
       `;
       $(listName).append(liStr);
     }
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


