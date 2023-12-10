/* r2dec pseudo code output */
/* great_old_talisman @ 0x40155f */
#include <stdint.h>
 
int32_t main (void) {
    size_t nbyte;
    eax = 0;
    setup ();
    banner ();
    printf("\nThis Great Old Talisman will protect you from the evil powers of zombies!\n\nDo you want to enchant it with a powerful spell? (1 -> Yes, 0 -> No)\n\n>> ");
    scanf ("%d", &nbyte);
    printf ("\nSpell: ");
    read (0, obj_talis + (int64_t) nbyte * 8, 2);
    al = exit (0x520);
    *(rax) += al;
}
