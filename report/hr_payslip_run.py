#coding: utf-8
#采购订单打印模板
import time
from openerp.report import report_sxw
from openerp.osv import osv
from openerp import pooler

class payslip_run(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(payslip_run, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({'time': time})

report_sxw.report_sxw('report.hr.payroll.payslip.run.xls','hr.payslip.run','addons/custom_hr_payroll/report/hr_payslip_run.mako',parser=payslip_run)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
