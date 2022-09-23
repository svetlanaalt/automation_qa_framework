import time

from generators.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self,):
        person_info = next(generated_person())

        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)

        self.element_is_visible(self.locators.SUBMIT).click()

        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name_str = self.element_is_present(self.locators.CREATED_OUTPUT_FORM).text.split("\n")[0]
        full_name = full_name_str.split(':')[1]
        email_str = self.element_is_present(self.locators.CREATED_OUTPUT_FORM).text.split("\n")[1]
        email = email_str.split(':')[1]
        current_address_str = self.element_is_present(self.locators.CREATED_OUTPUT_FORM).text.split("\n")[2]
        current_address = current_address_str.split(':')[1]
        permanent_address_str = self.element_is_present(self.locators.CREATED_OUTPUT_FORM).text.split("\n")[3]
        permanent_address = permanent_address_str.split(':')[1]

        return full_name, email, current_address, permanent_address
