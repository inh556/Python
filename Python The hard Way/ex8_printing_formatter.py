# -*- coding: utf-8 -*-
formatter = "%s %r %r %r"
print formatter % (1,2,3,4)
print formatter %('one', 'two','three','four')
print formatter %(True, False, False, True)
print formatter %(formatter, formatter,formatter,formatter)
print formatter %(
	"你好.",
	"That you could type up tonight.",
	"But it didn't sing.",
	"So, I said goodnight."
)