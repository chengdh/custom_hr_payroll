# -*- coding: utf-8 -*-

{
    'name': 'custom hr payroll',
    'version': '0.1',
    'category': 'Human Resources',
    'description': """定制工资表-for ktv""",
    'author': 'chengdh (cheng.donghui@gmail.com)',
    'website': '',
    'license': 'AGPL-3',
    'depends': ['hr_payroll','hr_expense','web'],
    'init_xml': [],
    'update_xml': ['data.xml','hr_payroll_view.xml','report.xml','hr_contract_view.xml'],
    'demo_xml': [],
    'active': False,
    'installable': True,
    'web':True,
    'css': [
      "static/src/css/defaultTheme.css",
      ],
    'js': [
      #"static/lib/jquery.mousewheel.js",
      "static/lib/jquery.fixedheadertable.min.js",
      "static/src/js/custom_hr_payroll.js",
      ],
    'xml': [],
}

