#coding: utf-8
%for p in objects:
<table style='border-collapse : collapse;border : 1px solid #000;'>
<thead>
    <tr><th colspan='26'><h3>${p.name}</h3></th></tr>
    <tr><th colspan='26'>${p.date_start}至${p.date_end}</th></tr>
    <tr>
    <th style='border : thin solid gray;'>部门</th>
    <th style='border : thin solid gray;'>姓名</th>
    <th style='border : thin solid gray;'>职务</th>
    <th style='border : thin solid gray;'>基本工资</th>
    <th style='border : thin solid gray;'>工龄工资</th>
    <th style='border : thin solid gray;'>试用天数</th>
    <th style='border : thin solid gray;'>实勤天数</th>
    <th style='border : thin solid gray;'>全勤奖金</th>
    <th style='border : thin solid gray;'>绩效工资</th>
    <th style='border : thin solid gray;'>加班天数</th>
    <th style='border : thin solid gray;'>酒水提成</th>
    <th style='border : thin solid gray;'>办卡提成</th>
    <th style='border : thin solid gray;'>再次分配</th>
    <th style='border : thin solid gray;'>其他奖励</th>
    <th style='border : thin solid gray;'>应发工资</th>
    <th style='border : thin solid gray;'>迟到早退</th>
    <th style='border : thin solid gray;'>未刷卡数</th>
    <th style='border : thin solid gray;'>旷工天数</th>
    <th style='border : thin solid gray;'>请假天数</th>
    <th style='border : thin solid gray;'>罚单扣除</th>
    <th style='border : thin solid gray;'>工装扣除</th>
    <th style='border : thin solid gray;'>班基扣除</th>
    <th style='border : thin solid gray;'>其他扣除</th>
    <th style='border : thin solid gray;'>扣除合计</th>
    <th style='border : thin solid gray;'>实发工资</th>
    <th style='border : thin solid gray;'>签字</th>
    </tr>
    </thead>
    <tbody>
   %for l in p.slip_ids: 
   <tr>
    <td style='border : thin solid gray;'>${l.employee_id.department_id.name or ""|entity}</td>
    <td style='border : thin solid gray;'>${l.employee_id.name}</td>
    <td style='border : thin solid gray;'>${l.employee_id.job_id.name or ""|entity}</td>
    <td style='border : thin solid gray;'>${l.basic}</td>
    <td style='border : thin solid gray;'>${l.year_salary}</td>
    <td style='border : thin solid gray;'>${l.trail_days}</td>
    <td style='border : thin solid gray;'>${l.worked_days}</td>
    <td style='border : thin solid gray;'>${l.work_prize}</td>
    <td style='border : thin solid gray;'>${l.prp}</td>
    <td style='border : thin solid gray;'>${l.ot}</td>
    <td style='border : thin solid gray;'>${l.dc}</td>
    <td style='border : thin solid gray;'>${l.cc}</td>
    <td style='border : thin solid gray;'>${l.rl}</td>
    <td style='border : thin solid gray;'>${l.os}</td>
    <td style='border : thin solid gray;'>${l.gross}</td>
    <td style='border : thin solid gray;'>${l.late}</td>
    <td style='border : thin solid gray;'>${l.no_sign}</td>
    <td style='border : thin solid gray;'>${l.absent_days}</td>
    <td style='border : thin solid gray;'>${l.leave_days}</td>
    <td style='border : thin solid gray;'>${l.punish_fee}</td>
    <td style='border : thin solid gray;'>${l.cloth_fee}</td>
    <td style='border : thin solid gray;'>${l.class_fee}</td>
    <td style='border : thin solid gray;'>${l.other_ded}</td>
    <td style='border : thin solid gray;'>${l.ded}</td>
    <td style='border : thin solid gray;'>${l.net}</td>
    <td style='border : thin solid gray;'>&nbsp;</td>
    </tr>
   %endfor
  </tbody>
  <tfoot>
    <tr>
    <td style='border : thin solid gray;' colspan='3'>合计</td>
    <td style='border : thin solid gray;'>${sum([l.basic for l in p.slip_ids])}</td>
    <td style='border : thin solid gray;'>${sum([l.year_salary for l in p.slip_ids])}</td>
    <td style='border : thin solid gray;'></td>
    <td style='border : thin solid gray;'>${l.worked_days}</td>
    <td style='border : thin solid gray;'>${sum([l.work_prize for l in p.slip_ids])}</td>
    <td style='border : thin solid gray;'>${sum([l.prp for l in p.slip_ids])}</td>
    <td style='border : thin solid gray;'>${sum([l.ot for l in p.slip_ids])}</td>
    <td style='border : thin solid gray;'>${sum([l.dc for l in p.slip_ids])}</td>
    <td style='border : thin solid gray;'>${sum([l.cc for l in p.slip_ids])}</td>
    <td style='border : thin solid gray;'>${sum([l.rl for l in p.slip_ids])}</td>
    <td style='border : thin solid gray;'>${sum([l.os for l in p.slip_ids])}</td>
    <td style='border : thin solid gray;'>${sum([l.gross for l in p.slip_ids])}</td>
    <td style='border : thin solid gray;'>${sum([l.late for l in p.slip_ids])}</td>
    <td style='border : thin solid gray;'>${sum([l.no_sign for l in p.slip_ids])}</td>
    <td style='border : thin solid gray;'>${sum([l.absent_days for l in p.slip_ids])}</td>
    <td style='border : thin solid gray;'>${sum([l.leave_days for l in p.slip_ids])}</td>
    <td style='border : thin solid gray;'>${sum([l.punish_fee for l in p.slip_ids])}</td>
    <td style='border : thin solid gray;'>${sum([l.cloth_fee for l in p.slip_ids])}</td>
    <td style='border : thin solid gray;'>${sum([l.class_fee for l in p.slip_ids])}</td>
    <td style='border : thin solid gray;'>${sum([l.other_ded for l in p.slip_ids])}</td>
    <td style='border : thin solid gray;'>${sum([l.ded for l in p.slip_ids])}</td>
    <td style='border : thin solid gray;'>${sum([l.net for l in p.slip_ids])}</td>
    <td style='border : thin solid gray;'>&nbsp;</td>
    </tr>
    <tr>
    <td colspan='26'>&nbsp;</td>
    </tr>
    <tr>
    <td colspan='26'>&nbsp;</td>
    </tr>
    <tr>
    <td colspan='5'>制表:</td>
    <td colspan='5'>审核:</td>
    <td colspan='5'>会计:</td>
    <td colspan='11'>总经理:</td>
    </tr>
  </tfoot>

</table>
%endfor
