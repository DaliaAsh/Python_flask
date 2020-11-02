const items = Array.from(document.getElementsByClassName("dashboard-item"));
items.map((item) => {
  item.addEventListener("click", function (event) {
    item.className = "highlight dashboard-item";
    let other_items = items.filter((element) => {
      return element !== item;
    });
    other_items.map((element) => {
      element.className = "dashboard-item";
    });
  });
});
const setPage = (pathname) => {
  console.log(pathname);
  window.location.href = pathname;
};
const sendDeleteRequest = (id, type) => {
  switch (type) {
    case "product":
      window.location.href = `/delete-product/${id}`;
      break;
    case "location":
      window.location.href = `/delete-location/${id}`;
      break;
    case "movement":
      window.location.href = `/delete-movement/${id}`;
      break;
  }
};
const sendUpdateRequest = (old_id, updated_id, type) => {
  switch (type) {
    case "product":
      window.location.href = `/update-product/${old_id}/${updated_id}`;
      break;
    case "location":
      window.location.href = `/update-location/${old_id}/${updated_id}`;
      break;
    case "movement":
      window.location.href = `/update-movement/${old_id}/${updated_id}`;
      break;
  }
};
