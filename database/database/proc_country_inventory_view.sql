drop view vw_country_inventry
;
create VIEW vw_country_inventry as
  SELECT
        s.Country,
        invtry.count as Stock_Count,
        YEAR(stmp.Issue_Date) as Year,
        s.Name as Set_Name,
        s.ID as Set_ID,
        s.Cardinality,
        stmp.Set_Member_ID as Member_ID,
        stmp.Name as Member_Name,
        stmp.Face_Value,
        stmp.FV_Denom
  FROM
        Stamps as stmp
          inner join Sets AS s on stmp.Set_ID=s.ID
          left outer join Inventory as invtry on stmp.Stamp_ID=invtry.Stamp_ID

;