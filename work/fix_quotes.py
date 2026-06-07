path = r'D:\www.jagmagh.com\jagmagh.github.io\inputs\build_v2.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

lq = '‘'  # left curly quote (opening delimiter, broken)
rq = '’'  # right curly quote (closing delimiter or content apostrophe)

# Line 308: h1([LQ]4. How the Role Has Changed[RQ])
# Replace with h1("4. How the Role Has Changed")
old1 = lq + '4. How the Role Has Changed' + rq
new1 = '"4. How the Role Has Changed"'

# Line 309: body([LQ]The table below...architect[RQ]s activities...valuable.[RQ])
# One RQ is the content apostrophe in "architect's", last RQ is the closing delimiter
body_inner = ('The table below compares the architect' + rq + 's activities before and after the '
    'widespread adoption of AI, and states why each has shifted. The pattern is consistent: '
    'where AI now produces the output or supplies the recall, the activity no longer requires '
    'an architect and can be delivered at developer level; where judgment, context, and '
    'accountability are required, the activity remains architect-level work and in several '
    'cases becomes more valuable.')
old2 = lq + body_inner + rq
# Convert RQ content apostrophe to straight, wrap in double quotes
new2 = '"' + body_inner.replace(rq, "'") + '"'

assert old1 in content, f"old1 not found: {repr(old1[:30])}"
assert old2 in content, f"old2 not found: {repr(old2[:50])}"

content = content.replace(old1, new1)
content = content.replace(old2, new2)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

remaining_lq = content.count(lq)
remaining_rq = content.count(rq)
print(f"Done. U+2018 remaining: {remaining_lq}, U+2019 remaining: {remaining_rq}")
