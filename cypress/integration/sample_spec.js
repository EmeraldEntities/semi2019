var fs = require('fs');

describe('My First Test', function() {
    it('Visits the Kitchen Sink', function() {  
      cy.visit('https://www.eventbrite.com/myevent?eid=80301061637')
      cy.request('https://www.eventbrite.com/myevent?eid=80301061637', 'followRedirect: true')
      cy.fixture('attendees.json').then((attendees) => {
        cy.wait(45000);
        for(var i = 0; i < 50; i++) {
          cy.get('#id_attendee_' + (i+1) + '_first_name').type(attendees[i].First)
          cy.get('#id_attendee_'+(i+1)+'_last_name').type(attendees[i].Last);
          cy.get('#id_attendee_'+(i+1)+'_email_address').type(attendees[i].Email)
        }
        cy.wait(20000)
        cy.get('a').contains('Complete Registration').click()
        cy.wait(20000)
      })
    })
    
  })