function loadChildChoices(parentField, child) {
    var valueField = child;
    var ajaxUrl = valueField.getAttribute("ajax_url");
    var emptyLabel = valueField.getAttribute('empty_label') || '--------';

    var headers = new Headers();
    headers.append("Accept", "application/json");

    var request = new Request(
        ajaxUrl + "?field=" + valueField.getAttribute("name") + "&parent_field=" + parentField.getAttribute("name") + "&parent_value=" + parentField.value,
        {
            method: "GET",
            headers: headers,
            credentials: 'same-origin'
        }
    );

    fetch(request).then(function(response) {
        return response.json();
    }).then(function(options) {
        var optionsHTML = "";

        if (!child[0].hasAttribute("multiple")) {
            optionsHTML += '<option value="">' + emptyLabel + '</option>';
        }

        options.forEach(function(option) {
            optionsHTML += '<option value="' + option[0] + '">' + option[1] + '</option>';
        });

        valueField.innerHTML = optionsHTML;
        valueField.dispatchEvent(new Event("change"));
        valueField.dispatchEvent(new Event("load"));
        valueField.dispatchEvent(new Event("liszt:updated")); // support for chosen versions < 1.0.0
        valueField.dispatchEvent(new Event("chosen:updated")); // support for chosen versions >= 1.0.0
    });
};

function loadAllChainedChoices(parentField) {
    var chained_ids = parentField.getAttribute('chained_ids').split(",");

    chained_ids.forEach(function(chained_id) {
        var child = document.getElementById(chained_id);
        loadChildChoices(parentField, child);
    });
};


document.addEventListener("DOMContentLoaded", function() {
    var parentFields = document.querySelectorAll(".chained-parent-field");

    parentFields.forEach(function(parentField) {
        if ( parentField.classList.contains('chzn-done') ) {
            $(parentField).change(function() {
                loadAllChainedChoices(this);
            });
        } else {
            parentField.addEventListener("change", function() { loadAllChainedChoices(this); });
        }
    });
});