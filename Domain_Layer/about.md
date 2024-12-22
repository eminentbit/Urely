# Architecture requirements 

The domains layer is the intermediary couch between the UI and data Layer , therefore , its missions are:
- Transform repository data into UI states
- Translate user interactions state changes
- Encapsulates Business Logic
- Decouples the Ui layer from the data Layer

To help you , you can break complex task into focuses operations by dividing them by uses cases .

## About the use cases 

You should keep the following in mind :
- Each one is a single responsibility class
- It has to be stateless
- It is injected into the UI layer

## This group is also responsible with Alexa shills 

Using the Alexa Skills Kit to build multilingual framework for at least 20 languages -selecting the most common spoken native languages -
