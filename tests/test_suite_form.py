from selene import browser, be, have, by


def test_form_01():
    """
    Заполнение формы
    Успешно заполнено
    """
    browser.open('/automation-practice-form')

    #form = browser.element('#practice-form-wrapper')
    browser.element('#firstName').type('FirstNameInput')
    browser.element('#lastName').type('LastNameInput')
    browser.element('#userEmail').type('emailName@contoso.com')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('0123456789')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('May')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('1970')).click()
    browser.element('.react-datepicker__day--029').click()
    browser.element('#subjectsInput').type('Phisics').press_enter()
    #browser.element('#subjectsInput').element(by.text('Phisics')).click()
    #browser.all('.subjects-auto-complete__menu').element_by(have.exact_text('Phisics')).click()
    #browser.element('#subjectsInput').context_click('Phisics')
    #browser.element('#firstName').type('NameInput')
    #browser.element('#firstName').type('NameInput')
    #browser.element('#firstName').type('NameInput')
    #browser.element('#firstName').type('NameInput')


