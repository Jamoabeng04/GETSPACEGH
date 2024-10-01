
function next(t){ 
    var parent = t.parentElement.parentElement.children[0]
    var item = parent.getElementsByClassName('item')
    parent.append(item[0])
}

function prev(t){
    var parent = t.parentElement.parentElement.children[0]
    var item = parent.getElementsByClassName('item')
    parent.prepend(item[item.length -1])
}




