let newChore = document.querySelector('#new-chore') //store value for chore
let choresList = document.querySelector('#chores-list') //list for displaying chores
let completeList = document.querySelector('#completed')

// function addItem () 

newChore.addEventListener('keyup', function(e) {
    if (e.key === "Enter") {
        let chore = newChore.value
        
        let newChoreItem = document.createElement('li')
        newChoreItem.innerText = chore
        choresList.appendChild(newChoreItem)
        choreDone = document.createElement('button')
        choreDone.setAttribute('done',chore)
        choreDone.innerText = 'Done'
        newChoreItem.appendChild(choreDone)
        choreDone.addEventListener('click',function() {
            newChoreItem.style.textDecoration = 'line-through'
            completeList.appendChild(this.parentElement)
            this.remove()
        })

        choreDel = document.createElement('button')
        choreDel.setAttribute('del',chore)
        choreDel.innerText = 'Delete'
        newChoreItem.appendChild(choreDel)
        choreDel.addEventListener('click',function() {
            this.parentElement.remove()
        })
    }      
}

)









    