#Укажем что это за фича
Feature: Checking book
#Укажем имя сценария (в одной фиче может быть несколько)
Scenario: Сheck some book in search results
#И используем наши шаги.
  Given website "https://www.amazon.com/"

  Then Filter should be selected : Book

  Then Type in search field : Java

  Then Check book on page

  Then close connection