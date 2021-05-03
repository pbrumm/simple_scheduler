FROM ubuntu:20.04

MAINTAINER palto42 <palto42@mailbox.org>

RUN apt-get -qq update && \
    apt-get -qq install git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN python3 -m venv /mnt/scheduler && \
    . /mnt/scheduler/bin/activate && \
    pip install -e git+https://github.com/palto42/simple_scheduler.git

ADD apns.pem /mnt/scheduler/
ADD run_scheduler /mnt/scheduler/bin/run_scheduler
RUN chmod 755 /mnt/scheduler/bin/run_scheduler

CMD ["/mnt/scheduler/bin/run_scheduler", "-s", "simple_scheduler.settings"]
