## Store Manager Application

[![Build Status](https://travis-ci.com/dorothykiz1/StoreManager.svg?branch=API)](https://travis-ci.com/dorothykiz1/StoreManager)

[![Coverage Status](https://coveralls.io/repos/github/dorothykiz1/StoreManager/badge.svg?branch=API)](https://coveralls.io/github/dorothykiz1/StoreManager?branch=API)

[![Maintainability](https://api.codeclimate.com/v1/badges/758c24d3971768f15921/maintainability)](https://codeclimate.com/github/dorothykiz1/StoreManager/maintainability)

-A web application that helps store owners manage sales and product inventory records
-This application is meant for use in a single store.

## Hosting

Follow this link to view the [Home page] https://dorothykiz1.github.io/StoreManager/

## Functionality

## Products

```
Get /products/
POST /products/
GET /products/<productId>

The Admin should be able to do the following:
1. Add a product to the product inventory
2. View all products in the product inventory
3. Get aspecific product from the inventory

The Sale attendant should be able to do the following:
1. View all products in the product inventory
2. Get aspecific product from the inventory


POST/products/<productId>
Expected parameters example: {"title":"three piece set","description":"Blue stripped three pice set with blaser","quantity":3}
```

## Sales

```
GET /sales/
POST /sales/
GET /sales/<saleId>

The Admin should be able to do the following:
1. View all products in the product inventory
2. Get aspecific sale record from the inventory

The Sale attendant should be able to do the following:
1. Add a sale record to the record inventory

POST/sales/<saleId>
Expected parameters example: {"attendant_Id":"21","attendant_name":"dee"}
```
