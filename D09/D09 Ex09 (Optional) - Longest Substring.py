str1 = str("AVOCADO")
str2 = str("CA")
# com_sub =
if len(str2) < len(str1):
    cache = str2
    str2 = str1
    str1 = cache
for letter in string:
    if letter in "AEIOUaeiou":
'''
if str2 in str1:
    print(str2 +" is a substring of "+ str1)
else: print(str1 +" is not a substring of "+ str2)
'''
# print("The longest common substring between "+ string1 +" and "+ string2 +"is ")
'''
var
    ans,cache,input1,input2:string;
    i,i2,long:integer;
begin

    for i:=0 to length(input1) do
    begin
        for i2:=0 to length(input1) do
        begin
            if (pos(copy(input1,i2,i),input2)>0) then
            begin
                if long<length(copy(input1,i2,i)) then
                begin
                    ans:=copy(input1,i2,i);
                    long:=length(copy(input1,i2,i));
                end;
            end;
        end;
    end;
    writeln(ans);
end.
'''