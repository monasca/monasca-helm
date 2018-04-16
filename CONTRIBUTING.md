# Contribution Guide

We're happy to accept contributions from the community. To do so, simply submit
a pull request to this repository.

## Signing Commits

We require a code sign-off for all contributions to indicate you have the right
to release any code as open-source. As explained by the [Docker project][1]:

> The sign-off is a simple line at the end of the explanation for the patch.
> Your signature certifies that you wrote the patch or otherwise have the right
> to pass it on as an open-source patch.

The agreement we use is the [Developer Certificate of Origin][1] (copied below),
as used by the Linux kernel, Docker, and many other open source projects:

```
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.
1 Letterman Drive
Suite D4700
San Francisco, CA, 94129

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.


Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.

```

Assuming you agree, simply add a line like the following to the end of each
commit message:

```
Signed-off-by: Joe Smith <joe.smith@email.com>
```

(note that we do need a real name here!)

For best results, use `git commit -s` to have this metadata added automatically
based on your configured Git name and email.

Ideally, all commits should also be [GPG signed][2], though we aren't strictly
enforcing this at the moment.

## Getting Help

For any contribution-related questions, please file an issue on this repository,
or ask in the `#openstack-monasca` channel on Freenode.

[1]: https://developercertificate.org/
[2]: https://help.github.com/articles/signing-commits-using-gpg/
