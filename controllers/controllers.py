# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
 class CustomAPI(http.Controller):
     @http.route('/custom_api/get_products',  auth='public')
     def get_products(self):
         print('entro a al servicio')
         product_rec = request.env['product.product'].search([])
         products =[]
         for rec in product_rec:
             vals = {
                 'id' = rec.id,
                  'code' = rec.code,
                 'name' = rec.name
                
             }
           
             products.add(vals)
         print('Lista =>',products)
         data = {'status':200,'response':products, 'message':'Success'}
         return data

  
