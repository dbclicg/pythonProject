
einspectitemrecord_sql = """select *
from (SELECT
             a.shopid                              AS "shopid"
      FROM einspectitemrecord@hgeb a
               left join operator@hgeb u on to_char(u.operatoroid) = a.check_user
      WHERE a.del_flag = '0'
        AND a.isqualified in (1)
        AND a.inspection_type = 123456454
      ORDER BY a.create_date DESC NULLS LAST)
where rownum = 1         ----本月已巡查记录=市场巡查"""
