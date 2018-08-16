Welcome to the FreeBSD archive!
-------------------------------

Here you will find the official releases of FreeBSD, along with
the ports and packages collection and other FreeBSD-related
material.  For those who have World Wide Web access, we encourage
you to visit the FreeBSD home page at:

   http://www.FreeBSD.org/


Contents of this directory:
---------------------------
releases/${ARCH}/*-RELEASE/
    The official FreeBSD releases.

    See README.TXT files in these directories for more information.
    The releases/${ARCH}/ISO-IMAGES directory also contains ISO 9660
    (+ rockridge extensions) installation CD images for the latest
    releases.  Please consider supporting the project and purchasing
    a FreeBSD CDROM from http://www.freebsdmall.com rather than burning
    your own ISO images.

snapshots/${ARCH}/*-YYMMDD-SNAP/
    Any "snapshot" tests of an upcoming release.  YYMMDD represents
    the year, month and day of the snapshot.  These are not frequently
    updated on this site for load reasons.  For the latest snapshots,
    see ftp://current.FreeBSD.org/pub/FreeBSD instead.

FreeBSD-current/
    This contains files relating to FreeBSD-current, which is
    the active development version of FreeBSD.  It is *strongly*
    advised that you be familiar with UNIX development in general
    and FreeBSD in particular before running this branch.

FreeBSD-stable/
    This contains files relating to FreeBSD-stable, the stable
    code branch of FreeBSD.

development/FreeBSD-CVS/
    This contains the FreeBSD CVS repository.  It is intended for
    use by developers.  However, a better way to update your CVS
    repository is with the cvsup tool.  See

      http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/cvsup.html

    for more information.

doc/
    Documentation for FreeBSD including the FAQ and the FreeBSD
    handbook.  Both these documents are available in hypertext
    form from http://www.FreeBSD.org/

ports/ports/
    A snapshot of the FreeBSD ports collection.  It contains
    makefiles, patches and configuration scripts necessary to make
    the applications in the distfiles/ directory compile and run
    on FreeBSD.  If your FreeBSD machine is connected to the
    Internet, you need not download the application source code
    from distfiles/ because the makefile will automatically fetch
    it for you.  A better way to update your ports collection is to use
    the cvsup tool: see 

      http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/cvsup.html

    for more information.

ports/${ARCH}/
    The FreeBSD package collection for supported architectures and
    FreeBSD branches.  These are pre-compiled applications ready
    to install with the pkg_add command.  Packages for recent
    releases are also included, but are not updated and are
    "frozen" to the state of the package collection at the time
    of release.

ports/distfiles/
ports/local_distfiles/
    Original source code distribution files for applications included
    in the ports collection.

tools/
    A collection of useful tools for people installing FreeBSD.
    This includes MS-DOS tools such as RAWRITE used for
    making installation disks, FIPS for splitting an MS-DOS
    partition and a couple boot managers to allow easy booting on
    computers with more than one operating system installed.


Mirror Sites:
-------------
The mirroring of FreeBSD distributions from this location is handled by
mapping each FreeBSD mirror into a common "namespace" which can be said
to follow this rule:

	ftp://ftp[n][.domain].FreeBSD.org/pub/FreeBSD

Where "n" is an optional, logical site number (when you have more than one
FTP server for a domain) and ".domain" is an optional domain, specifying
which particular region of the world you're interested in.  Examples:

	ftp://ftp3.FreeBSD.org/pub/FreeBSD	[3rd logical ftp mirror]
	ftp://ftp.fr.FreeBSD.org/pub/FreeBSD	[primary French mirror]
	ftp://ftp4.de.FreeBSD.org/pub/FreeBSD	[4th logical German mirror]

Logical site assignments are dynamic, with the "fastest, best connected"
mirrors having the lowest logical numbers.  The DNS administrators are
expected to keep this true as mirror sites are created or retired.


New Mirrors:
------------
If you create a new mirror of these FreeBSD distributions and wish to
make it more generally available, you should send mail to
hostmaster@FreeBSD.org and ask that your site be added to the
global logical namespace map (ftp://ftp[n].FreeBSD.org/pub/FreeBSD).

If the mirror is in a subdomain then mail must ALSO be sent to
hostmaster@domain.FreeBSD.org (where domain is your country's domain
designator) since each country is responsible for and "owns"
its own local DNS administration for domain.FreeBSD.org.

It also goes without saying that should you shut down a mirror
after so registering it, you're expect to send notice to these
addresses again so that the namespace can be updated.

Finally, you must make sure that all FreeBSD distributions are available
under the pub/FreeBSD hierarchy, as they are at ftp.FreeBSD.org.  This
can be a symbolic link or an actual directory, just so long as
the URL ``ftp://ftp[n][.domain].FreeBSD.org/pub/FreeBSD'' works
for your site (with appropriate values for "n" and ".domain").

That is an important requirement for automating the process of locating
and loading distributions from FreeBSD mirrors.

o What if my country does not have its own freebsd.org subdomain?

If that is your situation, you might well consider becoming
the DNS administrator for your country.  That person is responsible
for the day-to-day administration of ``somedomain.FreeBSD.org''
and should both be skilled in DNS setup and maintainence *and*
be contactable most days of the year since, essentially, any ftp or
www site in that country will be relying on the DNS administrator
to register and maintain the name space for the entire nation.

If you think you're qualified and there is no existing FreeBSD.org
subdomain for your country, please send email to the FreeBSD Hostmaster
(hostmaster@FreeBSD.org) and include details on your DNS server's IP
address and contact information for the DNS administrator.  As mentioned
above, you should also make sure that the hostmaster@yourdomain.FreeBSD.org
alias reaches the DNS administator since that address will be used by others
to report problems or submit new entries to the regional subdomain.
