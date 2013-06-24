#coding: utf-8
#重写hr_payroll,用于工资表显示
from openerp.osv import fields, osv
import logging

_logger = logging.getLogger(__name__)

class hr_payslip(osv.osv):
  '''
  工资条
  '''

  _name = 'hr.payslip'
  _inherit = 'hr.payslip'
  _description = 'Pay Slip'

  def _cal_salary_detail(self, cr, uid, ids, name, args, context):
        if not ids: return {}
        res = {}
        for payslip in self.browse(cr, uid, ids, context=context):
          lines_dict = {l.code.lower() : l.total for l in payslip.line_ids}
          res[payslip.id] = lines_dict

          ipt_dict = {ipt.code.lower() : ipt.amount for ipt in payslip.input_line_ids}
          res[payslip.id].update(ipt_dict)

          #工作时长
          if payslip.worked_days_line_ids:
            res[payslip.id]['worked_days'] = payslip.worked_days_line_ids[0].number_of_days
          else:
            res[payslip.id]['worked_days'] = 0

        return res


  _columns = {
    #基本工资
    "basic" : fields.function(_cal_salary_detail,method=True,multi='detail',string="基本工资",type='float',digits=(10,2)),
    #工龄工资
    "year_salary" : fields.function(_cal_salary_detail,method=True,multi='detail',string="工龄工资",type='float',digits=(10,2)),
    #试用天数
    "trail_days" : fields.function(_cal_salary_detail,method=True,multi='detail',string="试用天数",type='float',digits=(10,2)),
    #实勤天数
    "worked_days" : fields.function(_cal_salary_detail,method=True,multi='detail',string="实勤天数",type='float',digits=(10,2)),
    #全勤奖金
    "work_prize" : fields.function(_cal_salary_detail,method=True,multi='detail',string="全勤奖金",type='float',digits=(10,2)),
    #绩效工资
    "prp" : fields.function(_cal_salary_detail,method=True,multi='detail',string="绩效工资",type='float',digits=(10,2)),
    #加班天数
    "ot" : fields.function(_cal_salary_detail,method=True,multi='detail',string="加班天数",type='float',digits=(10,2)),
    #酒水提成
    "dc" : fields.function(_cal_salary_detail,method=True,multi='detail',string="酒水提成",type='float',digits=(10,2)),
    #办卡提成
    "cc" : fields.function(_cal_salary_detail,method=True,multi='detail',string="办卡提成",type='float',digits=(10,2)),
    #再次分配
    "rl" : fields.function(_cal_salary_detail,method=True,multi='detail',string="再次分配",type='float',digits=(10,2)),
    #其他奖励
    "os" : fields.function(_cal_salary_detail,method=True,multi='detail',string="其他奖励",type='float',digits=(10,2)),
    "alw" : fields.function(_cal_salary_detail,method=True,multi='detail',string="津贴合计",type='float',digits=(10,2)),
    #应发合计
    "gross" : fields.function(_cal_salary_detail,method=True,multi='detail',string="应发合计",type='float',digits=(10,2)),
    #迟到早退
    "late" : fields.function(_cal_salary_detail,method=True,multi='detail',string="迟到早退",type='float',digits=(10,2)),
    #未刷卡数
    "no_sign" : fields.function(_cal_salary_detail,method=True,multi='detail',string="未刷卡数",type='float',digits=(10,2)),
    #矿工天数
    "absent_days" : fields.function(_cal_salary_detail,method=True,multi='detail',string="旷工天数",type='float',digits=(10,2)),
    #请假天数
    "leave_days" : fields.function(_cal_salary_detail,method=True,multi='detail',string="请假天数",type='float',digits=(10,2)),
    #罚单扣除
    "punish_fee" : fields.function(_cal_salary_detail,method=True,multi='detail',string="罚单扣除",type='float',digits=(10,2)),
    #工装扣除
    "cloth_fee" : fields.function(_cal_salary_detail,method=True,multi='detail',string="工装扣除",type='float',digits=(10,2)),
    #班基金扣??
    "class_fee" : fields.function(_cal_salary_detail,method=True,multi='detail',string="班基金扣",type='float',digits=(10,2)),
    #其他扣除
    "other_ded" : fields.function(_cal_salary_detail,method=True,multi='detail',string="其他扣除",type='float',digits=(10,2)),
    #扣除合计
    "ded" : fields.function(_cal_salary_detail,method=True,multi='detail',string="扣除合计",type='float',digits=(10,2)),
    #实发工资
    "net" : fields.function(_cal_salary_detail,method=True,multi='detail',string="实发工资",type='float',digits=(10,2)),
  }


