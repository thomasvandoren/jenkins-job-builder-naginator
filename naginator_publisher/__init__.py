# -*- coding: utf-8 -*-

from jenkins_jobs.errors import JenkinsJobsException
import xml.etree.ElementTree as XML


def naginator(parser, xml_parent, data):
    """yaml: naginator
    Automatically reschedule a build after a build failure. Requires the
    Jenkins `Naginator Plugin
    <https://wiki.jenkins-ci.org/display/JENKINS/Naginator+Plugina>`_

    :arg int max-retries: Limits successive failed build retries. Set to 0 for
        no limit. Default is 0.
    :arg bool rerun-if-unstable: Rerun build for unstable builds as well as
        failures. Default is false.
    :arg dict delay: Must specify either fixed or progressive. Default is fixed
        with delay of 0.
        :delay:
            * **fixed** (`dict`)
                :fixed: * **delay** (`int`) seconds to wait before retrying (default: 0)
            * **progressive** (`dict`) Progressively delay before retrying
                build. The delay starts at *increment* seconds and grows by
                ``increment * number of consecutive failures`` up to the
                maximum value, then remains at *maximum*. e.g. (5, 10, 20,
                35, 55, ..., maximum) seconds.
                :progressive: * **increment** (`int`) - default is 0
                              * **maximum** (`int`) - default is 0
    :arg bool check-regexp: Only rerun build if regular expression is found in
        output. Default is false.
    :arg str regexp-for-rerun: Regular expression to search for.

    Example:

    .. literalinclude:: /../test/FIXME

    """
    root = XML.SubElement(
        xml_parent,
        'com.chikli.hudson.plugin.naginator.NaginatorPublisher'
    )

    XML.SubElement(root, 'maxSchedule').text = str(data.get('max-retries', 0))

    rerun_if_unstable = data.get('rerun-if-unstable', False)
    XML.SubElement(root, 'rerunIfUnstable').text = str(
        rerun_if_unstable).lower()

    delay = data.get('delay', {})
    fixed = delay.get('fixed')
    progressive = delay.get('progressive')

    if fixed is not None and progressive is not None:
        raise JenkinsJobsException(
            'Must specify one of fixed or progressive, not both.')
    elif fixed is None and progressive is None:
        # If no delay dict set, default to fixed with interval 0.
        fixed = {'delay': 0}

    delay_root = XML.SubElement(root, 'delay')
    if fixed is not None:
        delay_root.set('class',
                       'com.chikli.hudson.plugin.naginator.FixedDelay')
        XML.SubElement(delay_root, 'delay').text = str(fixed.get('delay', 0))
    elif progressive is not None:
        delay_root.set(
            'class', 'com.chikli.hudson.plugin.naginator.ProgressiveDelay')

        prg_increment = progressive.get('increment', 0)
        XML.SubElement(delay_root, 'increment').text = str(prg_increment)

        prg_maximum = progressive.get('maximum', 0)
        XML.SubElement(delay_root, 'max').text = str(prg_maximum)

    check_regexp = data.get('check-regexp', False)
    XML.SubElement(root, 'checkRegexp').text = str(check_regexp).lower()

    if not data.has_key('regexp-for-rerun'):
        XML.SubElement(root, 'regexpForRerun')
    else:
        XML.SubElement(root, 'regexpForRerun').text = data.get('regexp-for-rerun')
