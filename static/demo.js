function openTab(evt, target)
{
    var i, x;
    var tgt_id = target.split("-")[1]-1;
    x = document.getElementsByClassName("content-page");
    for (i=0; i < x.length; ++i)
    {
        x[i].style.display = "none";
    }

    var tabs = document.getElementsByClassName("nav-link");
    for (i=0; i < tabs.length; ++i)
    {
        tabs[i].classList.remove("active");
    }

    tabs[tgt_id].classList.add("active");
    document.getElementById(target).style.display = "block";
}

function updateWordTable(data)
{
    console.log(data);
}

function loadDataset(evt)
{
    data = document.getElementById("select-dataset");
    value = data.value;

    $.ajax({
        method: "GET",
        url: "loadDataset",
        data: {"data": value}
    }).done(function(msg){
        // Once data is loaded, get most shifted.
        $.ajax({
        method: "GET",
        url: "getMostShiftedWords",
        data: {"method": "global"}
            }).done(function(msg){
                console.log("words", msg);
            });
    });
}
