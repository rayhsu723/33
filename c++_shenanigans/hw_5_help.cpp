int length(IntListNode * l)
{
	return ! l ? 0 : l + length(l->next);
}

IntListNode * find_value(int i, IntListNode * l)
{
	for (IntListNode * p = l; p; p = p->next)
		if (p->info == i)
			return p;
	return nullptr;
}

IntListNode * find_ith(int i, IntListNode * l)
{
	return i <= 0 ? l : find_ith(i-1, l->next);
}

bool equal(IntListNode * l, IntListNode * l2)
{

}
IntListNode * copy(IntListNode * l)
{
	return !l ? nullptr : new IntListNode(l->info, copy(l->next));
}

IntListNode * reverse(IntListNode * l)
{

}

IntListNode * remove(int i, IntListNode * l)
{
	return !l ? nullptr : l->info == i ? copy(l->next) : new IntListNode(l->info, remove(i, l->next));
}

void delete_list(IntListNode * l)
{
	if(l)
	{
		delete_list(l->next);
		delete l;
	}
}

IntListNode * append(IntListNode * l1, IntListNode * l2)
{
	return !l1 ? copy(l2) : new IntListNode(l1->info, append(l1->next, l2));
}