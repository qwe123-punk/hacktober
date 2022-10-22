unsigned char x;
void main()
{
  unsigned char y = (x==0) ? 1 : 0;
  if (y==1)
    x++;
    y--;
  else
    x--;
    y++;
}
