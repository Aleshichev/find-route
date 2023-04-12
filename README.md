# Find Route
## Django project
### Django Bootstrap Docker

### Docker https://hub.docker.com/repository/docker/aleshichev/find_route/general

### Web http://aleshichev.pythonanywhere.com/post/7

#### The application can find the route of trains between cities. Displays the stations through which the train goes, calculates the shortest time.Suggests all possible routes.

## Resources
**Django**
**Django tests**
**Bootstrap 4.6.2**
**Js select2**
**SQlite**
**Postgresql**

## Project structure
**Django-project – Travel.**
- Settings : Local – SQlite, production - Postgresql

**App – Trains.**
- Creating, displaying and editing trains

**App – Routes.**
- Creating, displaying and editing routes. The application implements the logic of creating and displaying routes based on a graph.

**App – Cities.**
- Creating, displaying and editing cities

**App – Accounts.**
- Registration form, login - authorization form, exit function.
## The site has three types of display:
1. A non-registered user can browse pages and search for routes
2. The registered user can browse pages and search and save new routes.
3. Superuser can view and edit all sections of the site, and use the admin panel.

- There is an option to include logs
- The Routes application implements tests
