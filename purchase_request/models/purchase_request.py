from odoo import models, fields


class PurchaseRequest(models.Model):
    _name = 'purchase.request'
    _description = 'Purchase Request'
    _inherit = 'purchase.order'
    _rec_name = 'analytic_account_id'

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmation')],
        string='State',
        default='draft')

    analytic_account_id = fields.Many2one(
        'account.analytic.account',
        string='Analytical Account'
    )
    creation_date = fields.Datetime(
        string='Creation Date',
        readonly=True,
        default=lambda self: fields.datetime.now()
    )
    created_by = fields.Many2one(
        'res.users',
        string='Created By',
        readonly=True,
        default=lambda self: self.env.user.id
    )
    requested_by = fields.Many2one(
        'res.users',
        string='Requested By',
        default=lambda self: self.env.user.id
    )
    requested_on = fields.Date(
        string='Requested On',
        default=fields.Date.today(),
        required=True
    )
    purchase_request_lines_ids = fields.One2many(
        'purchase.request.lines',
        'purchase_request_id',
        string="Purchase Request Lines"
    )
    purchase_order_id = fields.Many2one(
        'purchase.order',
        string="Purchase Order"
    )
    purchase_order_ids = fields.One2many(
        'purchase.order',
        'purchase_request_id',
        string="Purchase Orders"
    )

    def confirm_action(self):
        self.state = 'confirm'
        for request in self:
            for line in request.purchase_request_lines_ids:
                vendor_id = line.vendor_id.id
                purchase_order = self.env['purchase.order'].search(
                    [('partner_id', '=', vendor_id), ('state', '=', 'draft')], limit=1)
                if not purchase_order:
                    purchase_order = self.env['purchase.order'].create({
                        'partner_id': vendor_id,
                        'date_planned': request.requested_on,
                    })
                self.env['purchase.order.line'].create({
                    'order_id': purchase_order.id,
                    'product_id': line.product_id.id,
                    'product_qty': line.quantity,
                    'product_uom': line.product_id.uom_id.id,
                    'price_unit': line.product_id.standard_price,
                })

    def cancel_action(self):
        self.state = 'draft'


class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    purchase_request_id = fields.Many2one(
        'purchase.request',
        string="Purchase Request"
    )
