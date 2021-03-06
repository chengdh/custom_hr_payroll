#coding: utf-8
#重写hr_payroll,用于工资表显示
from openerp.osv import fields, osv
import math
from datetime import datetime
import openerp.tools as tools
import logging

_logger = logging.getLogger(__name__)

class hr_payslip_run(osv.osv):
    _name = 'hr.payslip.run'
    _inherit = 'hr.payslip.run'
    _columns = {
        'slip_ids': fields.one2many('hr.payslip', 'payslip_run_id', 'Payslips',required=False, readonly=True, states={'draft': [('readonly', False)]}),
    }

class hr_payslip(osv.osv):
  '''
  工资条
  '''

  _name = 'hr.payslip'
  _inherit = 'hr.payslip'
  _description = 'Pay Slip'
  _order = "order_by"

  def _cal_salary_detail(self, cr, uid, ids, name, args, context):
        if not ids: return {}
        res = {}
        for payslip in self.browse(cr, uid, ids, context=context):
          lines_dict = {l.code.lower() : l.total for l in payslip.line_ids}
          res[payslip.id] = lines_dict

          _logger.debug("%s: "%lines_dict )
          ipt_dict = {ipt.code.lower() : ipt.amount for ipt in payslip.input_line_ids}
          res[payslip.id].update(ipt_dict)

          #工作时长
          #if payslip.worked_days_line_ids:
          #  res[payslip.id]['worked_days'] = payslip.worked_days_line_ids[0].number_of_days
          #else:
          #  res[payslip.id]['worked_days'] = 0

        _logger.debug("%s: %s"%(name,res) )

        return res

  def _cal_full_worked_days(self, cr, uid, ids, name, args, context):
    '''
    计算当月全勤天数,当月全勤天数 = 当月天数 - 3
    '''
    if not ids: return {}
    res = {}
    for payslip in self.browse(cr, uid, ids, context=context):
      d_to = datetime.strptime(payslip.date_to,tools.DEFAULT_SERVER_DATE_FORMAT)
      d_from = datetime.strptime(payslip.date_from,tools.DEFAULT_SERVER_DATE_FORMAT)
      month_days = (d_to - d_from).days
      res[payslip.id] = month_days - 3 + 1

    return res

  _columns = {
    #员工职务
    'job_id': fields.related('employee_id','job_id',type="many2one",relation="hr.job",string="职位",store=False),
    'order_by': fields.related('employee_id','job_id',"id",type="integer",string="职位",store=True),
    #基本工资
    "basic" : fields.function(_cal_salary_detail,method=True,multi='detail',string="基本工资",type='float',digits=(10,1)),
    #工龄工资
    "year_salary" : fields.function(_cal_salary_detail,method=True,multi='detail',string="工龄工资",type='float',digits=(10,1)),
    #试用天数
    "trail_days" : fields.function(_cal_salary_detail,method=True,multi='detail',string="试用天数",type='float',digits=(10,1)),
    "trail_days_input" : fields.integer(string="试用天数"),
    #实勤天数
    "worked_days" : fields.function(_cal_salary_detail,method=True,multi='detail',string="实勤天数",type='float',digits=(10,1)),
    "worked_days_input" : fields.integer(string="实勤天数"),
    #全勤奖金
    "work_prize" : fields.function(_cal_salary_detail,method=True,multi='detail',string="全勤奖金",type='float',digits=(10,1)),
    "work_prize_input" : fields.float(string="全勤奖金",digits=(10,1)),
    #绩效工资
    "prp" : fields.function(_cal_salary_detail,method=True,multi='detail',string="绩效工资",type='float',digits=(10,1)),
    "prp_input" : fields.float(string="绩效工资",digits=(10,1)),
    #加班天数
    "ot" : fields.function(_cal_salary_detail,method=True,multi='detail',string="加班天数",type='float',digits=(10,1)),
    "ot_input" : fields.integer(string="加班天数"),
    #酒水提成
    "dc" : fields.function(_cal_salary_detail,method=True,multi='detail',string="酒水提成",type='float',digits=(10,1)),
    "dc_input" : fields.float(string="酒水提成",digits=(10,1)),
    #办卡提成
    "cc" : fields.function(_cal_salary_detail,method=True,multi='detail',string="办卡提成",type='float',digits=(10,1)),
    "cc_input" : fields.float(string="办卡提成",digits=(10,1)),
    #再次分配
    "rl" : fields.function(_cal_salary_detail,method=True,multi='detail',string="再次分配",type='float',digits=(10,1)),
    "rl_input" : fields.float(string="再次分配",digits=(10,1)),
    #其他奖励
    "os" : fields.function(_cal_salary_detail,method=True,multi='detail',string="其他奖励",type='float',digits=(10,1)),
    "os_input" : fields.float(string="其他奖励",digits=(10,1)),
    #岗位津贴
    "job" : fields.function(_cal_salary_detail,method=True,multi='detail',string="岗位津贴",type='float',digits=(10,1)),
    "job_input" : fields.float(string="岗位津贴",digits=(10,1)),
    #津贴合计
    "alw" : fields.function(_cal_salary_detail,method=True,multi='detail',string="津贴合计",type='float',digits=(10,1)),
    "alw_disp" : fields.float(string="津贴合计",digits=(10,1)),
    #应发合计
    "gross" : fields.function(_cal_salary_detail,method=True,multi='detail',string="应发合计",type='float',digits=(10,1)),
    "gross_disp" : fields.float(string="应发合计",digits=(10,1)),
    #迟到早退
    "late" : fields.function(_cal_salary_detail,method=True,multi='detail',string="迟到早退",type='float',digits=(10,1)),
    "late_input" : fields.float(string="迟到早退",digits=(10,1)),
    #未刷卡数
    "no_sign" : fields.function(_cal_salary_detail,method=True,multi='detail',string="未刷卡数",type='float',digits=(10,1)),
    "no_sign_input" : fields.integer(string="未刷卡数"),
    #旷工天数
    "absent_days" : fields.function(_cal_salary_detail,method=True,multi='detail',string="旷工天数",type='float',digits=(10,1)),
    "absent_days_input" : fields.integer(string="旷工天数"),
    #请假天数
    "leave_days" : fields.function(_cal_salary_detail,method=True,multi='detail',string="请假天数",type='float',digits=(10,1)),
    "leave_days_input" : fields.integer(string="请假天数"),
    #罚单扣除
    "punish_fee" : fields.function(_cal_salary_detail,method=True,multi='detail',string="罚单扣除",type='float',digits=(10,1)),
    "punish_fee_input" : fields.float(string="罚单扣除",digits=(10,1)),
    #工装扣除
    "cloth_fee" : fields.function(_cal_salary_detail,method=True,multi='detail',string="工装扣除",type='float',digits=(10,1)),
    "cloth_fee_input" : fields.float(string="工装扣除",digits=(10,1)),
    #班基金扣??
    "class_fee" : fields.function(_cal_salary_detail,method=True,multi='detail',string="班基金扣",type='float',digits=(10,1)),
    "class_fee_input" : fields.float(string="班基金扣",digits=(10,1)),
    #其他扣除
    "other_ded" : fields.function(_cal_salary_detail,method=True,multi='detail',string="其他扣除",type='float',digits=(10,1)),
    "other_ded_input" : fields.float(string="其他扣除",digits=(10,1)),
    #扣除合计
    "ded" : fields.function(_cal_salary_detail,method=True,multi='detail',string="扣除合计",type='float',digits=(10,1)),
    "ded_disp" : fields.float(string="扣除合计",digits=(10,1)),
    #实发工资
    "net" : fields.function(_cal_salary_detail,method=True,multi='detail',string="实发工资",type='float',digits=(10,1)),
    "net_disp" : fields.float(string="实发工资",digits=(10,1)),
    #当月全勤天数,当月天数-3
    "full_worked_days" : fields.function(_cal_full_worked_days,method=True,string="全勤天数",type='integer'),
  }

  _defaults={
    #试用天数
    "trail_days_input" : 0,
    #实勤天数
    "worked_days_input" : 0,
    #全勤奖金
    "work_prize_input" : 0,
    #绩效工资
    "prp_input" : 0,
    #加班天数
    "ot_input" : 0,
    #酒水提成
    "dc_input" : 0,
    #办卡提成
    "cc_input" : 0,
    #再次分配
    "rl_input" : 0,
    #其他奖励
    "os_input" : 0,
    #岗位津贴
    "job_input" : 0,

    "late_input" : 0,
    #未刷卡数
    "no_sign_input" : 0, 
    #旷工天数
    "absent_days_input" : 0, 
    #请假天数
    "leave_days_input" : 0,
    #罚单扣除
    "punish_fee_input" : 0,
    #工装扣除
    "cloth_fee_input" : 0,
    #班基金扣??
    "class_fee_input" : 0,
    #其他扣除
    "other_ded_input" : 0,
    "alw_disp" : 0,
    "gross_disp" : 0,
    "ded_disp" : 0,
    "net_disp" : 0,
      }

  def  on_change_input(self,cr,uid,ids,input_code,input_val,context=None):
    input_line_pool = self.pool.get("hr.payslip.input")
    #根据传入的input_code,更新payslip_line中对应的input值
    for pslip in self.browse(cr,uid,ids,context):
      for l in pslip.input_line_ids:
        if l.code.lower()==input_code:
          input_line_pool.write(cr,uid,l.id,{'amount' : input_val})

    #调用compute_sheet重新计算工资,返回计算后的结果
    self.compute_sheet(cr,uid,ids,context)
    rs = self.read(cr,uid,ids,context)[0]
    res = {
        "alw_disp"     : math.floor(rs['alw']),
        "gross_disp"   : math.floor(rs['gross']),
        "ded_disp"     : math.floor(rs['ded']),
        "net_disp"     : math.floor(rs['net']),
        }
    return {"value" : res}
