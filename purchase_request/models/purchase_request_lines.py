from odoo import models, fields, api


class PurchaseRequestLines(models.Model):
    _name = 'purchase.request.lines'
    _description = 'Purchase Request Lines'

    product_id = fields.Many2one(
        'product.product',
        string="Product"
    )
    vendor_id = fields.Many2one(
        'res.partner',
        string="Vendor"
    )
    quantity = fields.Float(
        string="Quantity"
    )
    product_uom = fields.Many2one(
        'uom.uom',
        string='Unit of Measure',
        domain="[('category_id', '=', product_uom_category_id)]"
    )
    product_uom_category_id = fields.Many2one(
        related='product_id.uom_id.category_id'
    )
    purchase_request_id = fields.Many2one(
        'purchase.request',
        string="Purchase Request"
    )
