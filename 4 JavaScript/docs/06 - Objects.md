
# Objects

- [Overview](#overview)
- [Objects as Dictionaries](#objects-as-dictionaries)
- [Navigating Data](#navigating-data)


## Overview

In Python, there are separate data types for dictionaries, modules, instances of an object, and classes. In JavaScript all four of these functions use the same data type: objects. Let's take a look at how to use an object to store key/value pairs.

Objects are composed of primitive types. You can find more info on [mdn](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) and [w3schools](https://www.w3schools.com/js/js_objects.asp). 

```javascript
let contact = {
    first_name: 'Jane',
    last_name: 'Doe',
    age: 34
}
console.log(contact.first_name) // Jane
```

## Objects as Dictionaries

Objects can be used like dictionaries, but have attributes (variable names) instead of keys (strings). You can, however, use quotes around an attribute name like you would with strings.  This can allow you to use letters in keys that wouldn't ordinarily be possible, like leading numbers and hyphens.

```javascript
let contact = {
    name: 'Jane',
    '0': 'use a number as a key',
    'third-key': 'or use a hyphen'
}
console.log(contact.name) // Jane
console.log(contact['name']) // Jane
console.log(contact['0']) // use a number as a key
console.log(contact['third-key']) // or use a hyphen
```

## Navigating Data

```javascript
let library_user = {
    first_name: 'Jane',
    last_name: 'Smith',
    age: 20,
    books: [{
        title: 'A Wrinkle in Time',
        author: 'Madeleine L\'Engle',
        published: 1962
    },{
        title: 'The Giving Tree',
        author: 'Shel Silverstein',
        published: 1964
    }]
};
console.log(library_user.first_name); // Jane
console.log(library_user.books[0].title); // A Wrinkle in Time
```

