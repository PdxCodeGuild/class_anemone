# GLENN
(Grocery List Entry Nifty Navigator)

Other project name candidates:
- GLADYS (Grocery List App Does Your Shopping)
- GLINDA (Grocery List Interactive Navigation Deluxe App)


## Project Overview
Grocery shopping can be a chore sometimes, especially if you have a long grocery list or if you are shopping in a store that you've never been to before. Most people want to just get in and out as quickly and efficiently as possible, without having to roam through the grocery store searching for items. In addition, it would be nice to make the task of creating and maintaining a grocery list a little smoother too. The GLENN application is intended to organize your shopping list in such a way that streamlines your list-making and in-store shopping experience.


## Features
### User Stories and Associated Tasks
As a grocery shopper, I want to: 

**Minimum Viable Product 1**
1. Find the nearest grocery stores for my location so that I can easily find stores when I'm not in my neighborhood
    Tasks:
    - [ ]  Prompt user for zip code 
    - [ ]  Invoke Kroger Token API and obtain an access token 
    - [ ]  Invoke Kroger Locations API and pass in token and entered zip code 
    - [ ]  Display location results to user 
    - [ ]  Allow user to select their location 
2. Create and save a grocery list (add an item to my grocery list)
    - [ ]  Allow user to start a new grocery list and add items to their list 
    - [ ]  Store user's grocery list in database table, tied to the user, via Django REST Framework API
    - [ ]  Display new grocery list items as the user adds items to their list
    - [ ]  Display saved grocery list on load of the app
    - [ ]  Create "My List" sidebar menu item (or button)
3. Remove an item from my grocery list
    - [ ]  Include remove button next to each item on user's grocery list
    - [ ]  Remove corresponding record from database table for that grocery item via Django REST Framework API
4. Update a grocery list item
    - [ ]  Include edit button next to each item on user's grocery list
    - [ ]  Update corresponding record from database table for that grocery item via Django REST Framework API
5. Mark an item as complete so that I don't lose track of what I already have and what I still need to get
    - [ ]  Include action button with a checkmark icon next to each item on user's grocery list, if item isn't already marked as complete. 
    - [ ]  Move item to bottom of list and strikethrough the item name 

**Minimum Viable Product 2** *(Enhancement 1)*

6. Order my list items according to grocery store aisle so that I can walk the most efficient path through the grocery store possible (instead of going from aisle 1 to aisle 9 then aisle 3, etc.)
    - [ ]  Create button that allows user to order their grocery list when they are ready to go shopping 
    - [ ]  Invoke Kroger Products API and pass in token, location id, and product type 
    - [ ]  Alternate task for this capstone, if Kroger Products API doesn't work: Create and store product types and aisles in database and build Django REST Framework API to access this stored product/aisle info 
    - [ ]  Refresh grocery list on page and display ordered list 
    - [ ]  Include logic for slotting in periphery sections of store (produce, bakery, etc.) in ordered list 
7. Use GLENN to search for an item's aisle location while I am in the store so that I can quickly find an item that isn't on my list
    - [ ]  Create "Search for a grocery item" sidebar menu item 
    - [ ]  Allow user to enter in an item name (product type) and click a Search button 
    - [ ]  Display item name and aisle number
    - [ ]  Display "Add to List" button  

**Minimum Viable Product 3** *(Enhancement 2)*

8. Have a separate "The Usuals" list that is saved with my account that I can pull into my current grocery list so that I don't have to type the same items (like milk, eggs, etc.) every time I make a new list
    - [ ]  Include "Save to Usuals" action button next to each item on user's grocery list (regardless of whether item is considered completed or not) 
    - [ ]  Store item in database table with the grocery item
    - [ ]  Create "The Usuals" sidebar menu item so that user can see items on the usuals list
    - [ ]  Display "The Usuals" items when the usual requests it
9. Save special grocery lists (e.g. Thanksgiving dinner grocery list or a list for a specific recipe) so that I don't have to re-generate that special list every holiday or every time I make the same recipe
    - [ ]  Create "Save This List" action button so user can save this list in their stored/favorite lists
    - [ ]  Prompt user to create a name for their saved/favorites list
    - [ ]  Store each item in database table for that list
    - [ ]  Create "Favorites" sidebar menu item so that user can see stored/favorites lists
    - [ ]  Display grocery list items for the selected stored/favorites list when the user requests it
10. Type the first couple of letters for the item I want to add to my list (e.g. "ic") and have GLENN figure out the rest ("ice cream") so that I don't have to type in the entire item name.
    - [ ]  Store autocomplete guesses in database table for most common grocery items
    - [ ]  Create autocomplete logic that uses that stored autocomplete grocery item data

**Minimum Viable Product 4** *(Enhancement 3)*

11. Save my favorite grocery store so that I don't always have to "re-find" my neighborhood store
    - [ ]  Allow user to save their selected location to their user account
    - [ ]  Store selected favorite location in database table, tied to the user  
12. Share my list with others in my household that have a GLENN account
    - [ ]  Create "Share My List" sidebar menu item so that user can allow others to view/edit list
    - [ ]  Allow user to enter the GLENN user name if the person they want to share their list with
    - [ ]  Verify grantee is a valid GLENN user
    - [ ]  Allow user to see who they've shared their list with

**Minimum Viable Product 5** *(Enhancement 4)*

13. Optionally add a note to my grocery item
    - [ ]  Allow user to add a note about/for a grocery item on their list 
    - [ ]  Store note in database table with the grocery item 
14. ~~Optionally add a quantity or weight to my grocery item~~
    - [ ]  ~~Allow user to select a quantity or weight for a grocery item on their list~~ 
    - [ ]  ~~Store quantity/weight value/type in database table with the grocery item~~ 


## Data Model
**Grocery Item**

Purpose: Stores grocery item information and features

Columns/Attributes:
- item_id (PK, int)
- item_desc (char)
- aisle (char)
- usual (Boolean)
- item_note (char)
- create_date_time
- update_date_time


**Current Grocery List**

Purpose: Stores current grocery list

Columns/Attributes:
- list_id (PK, int)
- item_id (FK, int)
- store_location_id (int)
- aisle (char)
- create_date_time
- update_date_time


**Favorite Grocery List**

Purpose: Stores favorite grocery lists (holidays, recipes)

Columns/Attributes:
- list_id (PK, int)
- list_name (char)
- item_id (FK, int)
- favorite_name (char)


**User Location Preference**

Purpose: Stores the user's default store location 

Columns/Attributes:
- store_location_id


**User List Share**

Purpose: Stores the GLENN user_ids of users who are allowed to access a particular grocery list

Columns/Attributes:
- list_id (FK, int)
- share_with_user_id (int)
- create_date_time
- update_date_time


**Item Autocomplete**

Purpose: Stores grocery item name info, to assist with autocomplete functionality (not sure if this is necessary...need to research)

Columns/Attributes:
TBD


## Schedule
**MVP 1**
Estimate: 6 days

Major overhead tasks (other than what is noted above in 'User Stories and Associated Tasks' section above): Finish planning + set up all components (Django, DRF, Vue, etc) so that everything is talking to each other.

**MVP 2**
Estimate: 2 days

**MVP 3**
Estimate: 3 days

**MVP 4**
Estimate: 2 days

**MVP 5**
Estimate: 1 day
