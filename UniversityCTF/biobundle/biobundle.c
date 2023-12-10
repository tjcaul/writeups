/* r2dec pseudo code output */
/* biobundle @ 0x12aa */
#include <stdint.h>
 
int32_t main (void) {
	char * s1;
	uint32_t foo;
	int64_t handle;
	char buf [127];
	handle = get_handle ();
	foo = dlsym (handle, "_");
	if (foo == NULL) {
		return 0xffffffff;
	fgets (buf, 0x7f, stdin);
	buf[strcspn (buf, 0x0000201b)] = 0;
	if ((*foo)(buf) != 0) {
		puts ("[*] Untangled the bundle");
	} else {
		puts ("[x] Critical Failure");
	}
	return 0;
}
/* r2dec pseudo code output */
/* biobundle @ 0x11b5 */
#include <stdint.h>

char data [] = {
	//0x3e07 bytes of something
}

uint64_t get_handle (void) {
	char c; //rbp-0x1021
	char * s; //rbp-0x1020
	int64_t foo; //rbp-0x1018
	int64_t bar; //rbp-0x1010
	uint32_t baz; //rbp-0x18
	uint32_t fd; //rbp-0xc
	int i;

	fd = memfd_create (":^)", 0);
	if (fd == 0xffffffff) {
		exit (0xffffffff);
	}

	for (i = 0; i <= 0x3e07; ++i) {
		c = data[i] ^ 0x37;
		write (fd, &c, 1);
	}
	*s = 0;
	foo = 0;
	for (int j = 0; j < 510; ++j)
		bar[j] = 0;
	sprintf(s, "/proc/self/fd/%d", fd);
	baz = dlopen (s, 1);
	if (baz == 0) {
		exit (0xffffffff);
	}
	return baz;
}
