$$("li.countrylist-item a")
    .map(x => {
        return x.getAttribute("href").replace(/\//g, "");
    })