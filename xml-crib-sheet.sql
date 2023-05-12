
declare @somexml xml = '
<root>
    <element1 attribute="X">Element One</element1>
    <element2 attribute="Y">Element Two</element2>
    <element3 attribute="A">Element Three - Attribute A</element3>
    <element3 attribute="B">Element Three - Attribute B</element3>
    <element3 attribute="C">Element Three - Attribute C</element3>
    <element4>
        <nested attribute="4a">One level deep in 4a</nested>
        <nested attribute="4b">One level deep in 4b</nested>
        <nested attribute="4c">One level deep in 4c</nested>
        <nested attribute="4d">
            <nested-again>
            howdy
            </nested-again>
        </nested>
        <series>
            <row><col1>D</col1><col2>E</col2><col3>F</col3></row>
            <row><col1>G</col1><col2>H</col2><col3>I</col3></row>
            <row><col1>J</col1><col2>K</col2><col3>L</col3></row>
            <row><col1>M</col1><col2>N</col2><col3>O</col3></row>
        </series>
    </element4>
</root>'

-- insert into DocumentImport (EntryDate, Content) values (getdate(), @somexml)


-- Query to get entire doc/fragment
select @somexml.query('.')

-- Query to get a portion of doc/fragment
select @somexml.query('/root/element4');

-- Query to get series, no document root
select @somexml.query('/root/element4/nested');

-- Value from an element
select @somexml.value('(/root/element1)[1]', 'varchar(20)');

-- Value from an attribute of a element
select @somexml.value('(/root/element1/@attribute)[1]', 'varchar(20)');

-- Value from an element qualified (filtered) by an attribute value
select @somexml.value('(/root/element4/nested[@attribute="4b"])[1]', 'varchar(20)');

-- Value from an element qualified by index
select @somexml.value('(/root/element4/nested)[3]', 'varchar(20)');

-- Value from an element qualified (filtered) by an attribute value
select @somexml.value('(/root/element4/nested[@attribute="4b"])[1]', 'varchar(20)');


-- A projection from a series of elements in the xml variable
select series.value('(col1)[1]', 'varchar(20)') 'col1',
       series.value('(col2)[1]', 'varchar(20)') 'col2',
       series.value('(col3)[1]', 'varchar(20)') 'col3'
  from @somexml.nodes('/root/element4/series/row') as t2(series);


-- A projection from a series of elements in the xml table column
select t1.Id,
       series.value('(col1)[1]', 'varchar(20)') 'col1',
       series.value('(col2)[1]', 'varchar(20)') 'col2',
       series.value('(col3)[1]', 'varchar(20)') 'col3'
  from DocumentImport t1
 cross apply t1.Content.nodes('/root/element4/series/row') as t2(series);


/*
if exists (select 1 from sysobjects where name = 'ParsedXml')
  drop view ParsedXml
go

create view ParsedXml as
select t1.Id,
       series.value('(col1)[1]', 'varchar(20)') 'col1',
       series.value('(col2)[1]', 'varchar(20)') 'col2',
       series.value('(col3)[1]', 'varchar(20)') 'col3'
  from DocumentImport t1
 cross apply t1.Content.nodes('/root/element4/series/row') as t2(series);
*/

select * from ParsedXml