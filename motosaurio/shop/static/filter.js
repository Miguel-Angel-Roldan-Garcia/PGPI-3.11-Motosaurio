
function handleCheckboxClick(clickedCheckboxId, selectorExtraClass) {
  const checkboxes = Array.from(document.getElementsByClassName('form-check-input ' + selectorExtraClass));
  
  checkboxes.forEach(checkbox => {
    if (checkbox.id !== clickedCheckboxId) {
      checkbox.checked = false;
    }
  });
}

function searchFilter(order) {
  var searchInputElement = document.getElementById("searchInput");
  const checkboxesType = Array.from(document.getElementsByClassName('form-check-input product-type'));
  const checkboxesProducer = Array.from(document.getElementsByClassName('form-check-input producer'));

  query = [];
  if(searchInputElement && searchInputElement.value) {
    query.push("name=" + searchInputElement.value);
  }

  checkboxesType.forEach(checkbox => {
    if (checkbox.checked) {
      query.push("product_type=" + checkbox.value);
    }
  });

  checkboxesProducer.forEach(checkbox => {
    if (checkbox.checked) {
      query.push("producer=" + checkbox.value);
    }
  });
  
  if(order) {
    query.push("order=" + order)
  }

  var currentUrl = window.location.href.split("?")[0];
  var newUrl = currentUrl + "?" + query.join("&");
  window.location.href = newUrl;
}
  
function search() {
  var queryString = window.location.search.substring(1);
  var params = queryString.split('&');
  var orderQuery = null
  for (var i = 0; i < params.length; i++) {
      var pair = params[i].split('=');
      if (pair[0] === "order") {
          orderQuery = decodeURIComponent(pair[1]);
      }
  }
  searchFilter(orderQuery)
}
