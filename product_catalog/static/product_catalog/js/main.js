```javascript
$(document).ready(function() {
    // Function to handle search feature
    function search_product() {
        let query = $("#search-input").val();
        $.ajax({
            url: '/search/',
            data: {
                'search_text': query,
            },
            dataType: 'json',
            success: function(data) {
                // Render the search results
            }
        });
    }

    // Function to handle alternative search feature
    function alternative_search() {
        let query = $("#alternative-search-input").val();
        $.ajax({
            url: '/alternative_search/',
            data: {
                'search_text': query,
            },
            dataType: 'json',
            success: function(data) {
                // Render the alternative search results
            }
        });
    }

    // Function to handle export feature
    function export_list() {
        $.ajax({
            url: '/export/',
            dataType: 'json',
            success: function(data) {
                // Handle the exported data
            }
        });
    }

    // Event listeners
    $("#search-button").click(search_product);
    $("#alternative-search-button").click(alternative_search);
    $("#export-button").click(export_list);
});
```