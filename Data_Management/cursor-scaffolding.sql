

create table sometable
(
    boo         varchar(03)         null,
    foo         int                 null,
    soo         date                null
)
go
create unique index AK1sometable on sometable (boo) where boo is not null
go


insert into sometable values
('abc', 1, '1900-01-01'),
('def', 2, '1970-01-01'),
('ghi', 3, '2000-01-01'),
(null,  4, '1900-01-01'),
(null,  5, '1970-01-01'),
(null,  6,'2000-01-01'),
('jkl', null, '1900-01-01'),
('mno', null, '1970-01-01'),
('pqr', null, '2000-01-01'),
('stu', 7, null),
('vwx', 8, null),
('yz0', 9, null)


-- declare vars to hold column values returned by cursor
-- these variable names do not have to match the table
-- column names, but they should match the data type, or
-- be such that they allow an implicit conversion, e.g.,
-- string -> date

declare @col1       varchar(10),
        @col2       int,
        @col3       date


-- declare the cursor
declare curs_sometable cursor local forward_only read_only for
select boo, foo, soo
  from sometable
 where 1 = 1
 order by soo, foo

-- open the cursor
open curs_sometable

-- fetch the current row from the cursor
-- and put column values into the vars
fetch next from curs_sometable into @col1, @col2, @col3

-- iterate over the cursor until there are no
-- more rows, i.e., @@fetch_status != 0
while @@fetch_status = 0
begin

    print 'do some stuff here with @col1 = ' + isnull(@col1, '<null>') + ', @col2 = ' + isnull(cast(@col2 as varchar), '<null>') + ', @col3 = ' + isnull(cast(@col3 as varchar), '<null>')

    -- done with current row, so advance cursor to
    -- next row and put new column values in vars

    fetch next from curs_sometable into @col1, @col2, @col3
end

-- out of the loop, done with cursor, so close it
-- and deallocate to free up the server resources
close curs_sometable
deallocate curs_sometable