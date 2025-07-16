Project : Leetcode Tracker

What : The goal is to build a leetcode tracking assistant that
1. Keeps track of when you submit a new problem
2. Keeps track of the related topics and prompts you to do active recall
3. Integrates with telegram bot to remind you to do tasks active recall
4. Integrates with notion and maybe other third parties such as google sheets to automate workflows

High level design:
1. leetcode uses a public graphql endpoint
2. Our backend will be written in flask and wrap the relevant endpoints to allow easy integration with other third party api services
