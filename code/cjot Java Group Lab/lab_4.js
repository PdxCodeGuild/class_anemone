// let delta = document.getElementById('delete')
// let omega = document.getElementById('create')
// let mark = document.getElementById('completed')
let nitems = document.getElementsByClassName('nitem')
let itemDiv = document.getElementById('todoitem')
let Confirm = document.getElementById('submit')

Confirm.addEventListener('click', function() {
    let addeditem = document.getElementById('nitem')
    addeditem.classList.add('nitem')
    itemDiv.appendChild(addeditem)
    console.log(addeditem)
    // let newtext = document.createTextNode()
    // let item1 = document.getElementById('')
})

// Confirm.addEventListener('click', function() {
//     let todoitem=document.getElementById('item')
//     let completed=document.getElementById('citem')
//     let newitem=document.getElementById('nitem')
//     console.log(todoitem, completed, newitem)
    
//     delta.addEventListener('click', function() {
//         let something = 'import data'
//     })

//     omega.addEventListener('click', function() {
//         let something = 'import data'
//     })

//     // mark.addEventListener('click', function() {
//     //     let something = 'import data'
//     // })
// })


