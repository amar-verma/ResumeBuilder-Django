
        document.getElementById('profile-photo').onclick = function() {
            document.getElementById('photo-upload').click();
        };
        document.getElementById('photo-upload').onchange = function(event) {
            if (event.target.files && event.target.files[0]) {
                var reader = new FileReader();
                reader.onload = function(e) {
                    document.getElementById('profile-photo').src = e.target.result;
                };
                reader.readAsDataURL(event.target.files[0]);
            }
        };
