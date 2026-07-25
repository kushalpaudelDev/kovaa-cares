(function(){
  function showError(el,msg){
    el.classList.add('field-error');
    var id = el.id || (el.name && ('id-'+el.name));
    var err = el.closest('.field')?.querySelector('.error-text');
    if(!err){
      err = document.createElement('div'); err.className='error-text';
      (el.closest('.field')||el.parentNode).appendChild(err);
    }
    err.textContent = msg;
  }
  function clearError(el){
    el.classList.remove('field-error');
    var err = el.closest('.field')?.querySelector('.error-text');
    if(err) err.textContent = '';
  }
  function validateForm(form){
    var valid = true;
    var reqs = form.querySelectorAll('[required]');
    reqs.forEach(function(input){
      clearError(input);
      if(!input.value.trim()){
        showError(input, 'This field is required');
        valid=false;
      }
    });
    var email = form.querySelector('input[type="email"]');
    if(email && email.value){
      var re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if(!re.test(email.value)){
        showError(email,'Enter a valid email'); valid=false;
      }
    }
    var pw1 = form.querySelector('input[name="password1"]');
    var pw2 = form.querySelector('input[name="password2"]');
    if(pw1 && pw2){
      clearError(pw2); clearError(pw1);
      if(pw1.value !== pw2.value){ showError(pw2,'Passwords do not match'); valid=false; }
    }
    return valid;
  }
  document.addEventListener('submit', function(e){
    var form = e.target;
    if(form.matches('form')){
      var doValidate = form.dataset.validate !== 'off';
      if(doValidate){
        if(!validateForm(form)){
          e.preventDefault();
          var firstError = form.querySelector('.field-error');
          if(firstError) firstError.focus();
        }
      }
    }
  }, true);
})();
