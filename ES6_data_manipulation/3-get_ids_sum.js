export default function getStudentIdsSum(students) {
  return students.reduce((some, student) => some + student.id, 0);
}
