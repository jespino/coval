CodVal: Code Valididator
========================

CodVal is a library to validate alphanumeric codes like IBAN, ISBN,
SSN, Postal Codes, etcetera. Is based on the Validate PHP Pear project and try
to be an internacional library that have localized validations for countries
internal codes like DNI in spain.

Usage
=====

CodVAl have a modular design, based on one module per country (with iso2
country code as name), and a international module for not strictly national
codes validators.

All functions have a optional parameter "strict" that if is False, will ignore
characters like '-', '/' or spaces, depending on the code to validate.
