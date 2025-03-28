import { expect } from 'chai';
import sinon from 'sinon';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;
  let consoleSpy;

  before(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    queue.testMode.clear();
    consoleSpy.resetHistory();
  });

  after(() => {
    queue.testMode.exit();
    consoleSpy.restore();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw(
      'Jobs is not an array'
    );
  });

  it('should create jobs in the queue', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'Test message 1' },
      { phoneNumber: '4153518781', message: 'Test message 2' }
    ];

    createPushNotificationsJobs(jobs, queue);

    // Verify jobs were created
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
    expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);

    // Verify console logs
    expect(consoleSpy.calledWith('Notification job created: 1')).to.be.true;
    expect(consoleSpy.calledWith('Notification job created: 2')).to.be.true;
  });
});