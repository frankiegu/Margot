#! /usr/bin/perl

use strict;
use warnings;

# Getting command line arguments:
use Getopt::Long;
# Documentation:
use Pod::Usage;
# I/O Handler
use IO::Handle;

use locale;
use POSIX qw(locale_h);
setlocale(LC_ALL,"");

use FindBin;
use lib "$FindBin::Bin";

require 'english-utils.pl';

## Create a list of words and their frequencies from an input corpus document
## (format: plain text, words separated by spaces, no sentence separators)

## TODO should words with hyphens be expanded? (e.g. three-dimensional)


while (<>) {


    chomp($_);
    my @words = split(" ", $_);

    foreach my $word (@words) {

        # Check validity against regexp and acceptable use of apostrophe

        if (($word =~ /^[a-z][a-z\'-]*$/ || $word eq "<s>" || $word eq "</s>") && (index($word,"'") < 0 || allow_apostrophe($word))) {
       		print $word." "
	 }
    }
	print "\n"
}


